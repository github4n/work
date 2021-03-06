var test = function(url,cid,uuid) {
    const rawHeaderLen = 16;
    const packetOffset = 0;
    const headerOffset = 4;
    const verOffset = 6;
    const opOffset = 8;
    const seqOffset = 12;

    var Client = function(options) {
        var MAX_CONNECT_TIMES = 10;
        var DELAY = 15000;
        this.options = options || {};
        this.createConnect(MAX_CONNECT_TIMES, DELAY);
    }

    Client.prototype.createConnect = function(max, delay) {
        var self = this;
        if (max === 0) {
            return;
        }
        connect();

        var textDecoder = new TextDecoder();
        var textEncoder = new TextEncoder();
        var heartbeatInterval;
        function connect() {
            var ws = new WebSocket(url);  //new WebSocket('ws://192.168.23.13:8090/sub');
            ws.binaryType = 'arraybuffer';
            ws.onopen = function() {
                auth();
            }

            ws.onmessage = function(evt) {
                var data = evt.data;
                var dataView = new DataView(data, 0);
                var packetLen = dataView.getInt32(packetOffset);
                var headerLen = dataView.getInt16(headerOffset);
                var ver = dataView.getInt16(verOffset);
                var op = dataView.getInt32(opOffset);
                var seq = dataView.getInt32(seqOffset);

//                console.log("receiveHeader: packetLen=" + packetLen, "headerLen=" + headerLen, "ver=" + ver, "op=" + op, "seq=" + seq);

                switch(op) {
                    case 8:                                      // batch message
                        for (var offset=0; offset<data.byteLength; offset+=packetLen) {
                            // parse
                            var packetLen = dataView.getInt32(offset);
                            var headerLen = dataView.getInt16(offset+headerOffset);
                            var ver = dataView.getInt16(offset+verOffset);
                            var msgBody = textDecoder.decode(data.slice(offset+headerLen, offset+packetLen));
                            console.log(msgBody);
                            // callback
                            messageReceived(ver, msgBody);
                        }
                        // heartbeat
                        // heartbeat
                        heartbeat();
                        heartbeatInterval = setInterval(heartbeat, 30 * 1000);
                    break;
                    case 3:
                        // heartbeat reply
//                        console.log("receive: heartbeat");
                    break;
                    case 5:
                        // batch message
                        for (var offset=0; offset<data.byteLength; offset+=packetLen) {
                            // parse
                            var packetLen = dataView.getInt32(offset);
                            var headerLen = dataView.getInt16(offset+headerOffset);
                            var ver = dataView.getInt16(offset+verOffset);
                            var msgBody = textDecoder.decode(data.slice(offset+headerLen, offset+packetLen));
                            // callback
                            messageReceived(ver, msgBody);
                        }
                    break;
                }
            }

            ws.onclose = function() {
                if (heartbeatInterval) clearInterval(heartbeatInterval);
                setTimeout(reConnect, delay);
            }

			
			
			
	
            function heartbeat() {
                var headerBuf = new ArrayBuffer(rawHeaderLen);
                var headerView = new DataView(headerBuf, 0);
                headerView.setInt32(packetOffset, rawHeaderLen);
                headerView.setInt16(headerOffset, rawHeaderLen);
                headerView.setInt16(verOffset, 1);
                headerView.setInt32(opOffset, 2);
                headerView.setInt32(seqOffset, 1);
                ws.send(headerBuf);
//                console.log("send: heartbeat");
            }
			
			
			const rawHeaderLen = 16;
			const packetOffset = 0;
			const headerOffset = 4;
			const verOffset = 6;
			const opOffset = 8;
			const seqOffset = 12;
	
            function auth() {
                var tokenBody = {"Uid":parseInt(uuid),"Rid":parseInt(cid)};
                var token = JSON.stringify(tokenBody);
                var headerBuf = new ArrayBuffer(rawHeaderLen);
                var headerView = new DataView(headerBuf, 0);
                var bodyBuf = textEncoder.encode(token);
//                console.log(bodyBuf.byteLength);

                headerView.setInt32(packetOffset, rawHeaderLen + bodyBuf.byteLength);
                headerView.setInt16(headerOffset, rawHeaderLen);
                headerView.setInt16(verOffset, 1);
                headerView.setInt32(opOffset, 7);
                headerView.setInt32(seqOffset, 1);
				
				var mergeA = mergeArrayBuffer(headerBuf, bodyBuf);
//				console.log("mergeA", headerView.getInt32(0),  headerView.getInt16(4),  headerView.getInt16(6),  headerView.getInt32(8),  headerView.getInt32(12));
//
//				console.log(headerBuf);
//				console.log(bodyBuf);
//				console.log(100,mergeA);

				// console.log(textEncoder.decode(bodyBuf));

                ws.send(mergeA);
//                console.log(1000);


            }

            function messageReceived(ver, body) {
//                console.log("messageReceived:", "ver=" + ver, "body=" + body);
                var notify = self.options.notify;
                if(notify) notify(body);

            }

            function mergeArrayBuffer(ab1, ab2) {
                var u81 = new Uint8Array(ab1),
                    u82 = new Uint8Array(ab2),
                    res = new Uint8Array(ab1.byteLength + ab2.byteLength);
                res.set(u81, 0);
                res.set(u82, ab1.byteLength);
                return res.buffer;
            }

            function char2ab(str) {
                var buf = new ArrayBuffer(str.length);
                var bufView = new Uint8Array(buf);
                for (var i=0; i<str.length; i++) {
                    bufView[i] = str[i];
                }
                return buf;
            }

        }

        function reConnect() {
            self.createConnect(--max, delay * 2);
        }
    }

    window.MyClient = Client;

};


function isJsonString(str) {
        try {
            if (typeof JSON.parse(str) == "object") {
                return true;
            }
        } catch(e) {
        }
        return false;
    }



function getQueryString(name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) return unescape(r[2]);
        return 2;
    }


url = getQueryString('url'); //'ws://gate.huomaotv.com.cn:8090/sub'
cid = getQueryString('cid');
uuid = getQueryString('uid');
console.log('连接url:',url);
console.log('连接cid:',cid);
console.log('连接uid:',uuid);
test(url,cid,uuid);

var html = '';
var client = new MyClient({

    notify: function(data) {
        if(isJsonString(data)){
        data = JSON.parse(data);
        html += '<pre style="margin:10px;font-size: 12px;max-height:50px;max-width:1200px;" class="pre-scrollable">'+ JSON.stringify(data,null,4) +'</pre>';
        console.log(data);
        $(".test").html(html);}else{
            console.log(data);
        }
    }

});

$(document).on("mouseover",".pre-scrollable",function(){
//    $(this).stop().animate({'max-height':'800px'},500);
    $(this).css("max-height","800px")
});
$(document).on("mouseout",".pre-scrollable",function(){
    $(this).stop().animate({'max-height':'50px'},500);
//    $(this).css("max-height","50px")
});