function request(method){
    switch(method){
        case 'set_money':
            url = '/new_web/set_money';
            data = $("#set_money_form").serialize()
            break;
        case 'bd_sj':
            url = '/new_web/bd_sj';
            data = $("#bd_sj_form").serialize()
            break;
        case 'zc':
            url = '/new_web/zc';
            data = $("#zc_form").serialize()
            break;
        case 'sq_zb':
            url = '/new_web/sq_zb';
            data = $("#sq_zb_form").serialize()
            break;
        case 'update_stream':
            url = '/new_web/update_stream';
            data = $("#update_stream_form").serialize()
            break;
        case 'update_stat':
            url = '/new_web/update_stat';
            data = $("#update_stat_form").serialize()
            break;
        case 'update_roomlx':
            url = '/new_web/update_roomlx';
            data = $("#update_roomlx_form").serialize()
            break;
        case 'find_uid':
            url = '/new_web/find_uid';
            data = $("#find_uid_form").serialize()
            break;
        case 'init_fans':
            url = '/new_web/init_fans'
            data = $("#init_fans_form").serialize()
            break;
        case 'update_password':
            url = '/new_web/update_password'
            data = $("#update_password_form").serialize()
            break;
    }
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        async: false,
        success: function(result) {
            $('.modal-body').text(result.msg);
            $('#myModal').modal('show');
            setTimeout(function(){$("#myModal").modal("hide")},1000);
        }
    });
}

//
//
//function bd_sj() {
//    id_name = $("#id_name2").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/bd_sj',
//        data: { 'id_name': id_name },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}
//
//function zc() {
//    id_name = $("#id_name3").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/zc',
//        data: { 'id_name': id_name },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}
//
//function sq_zb() {
//    id_name = $("#id_name4").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/sq_zb',
//        data: { 'id_name': id_name },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}
//
//function update_stream() {
//    room_number_online = $("#id_name5").val();
//    room_number_offine = $("#id_name6").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/update_stream',
//        data: { 'room_number_online': room_number_online, 'room_number_offine': room_number_offine },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}
//
//function phone_fy() {
//    cid = $("#id_fy1").val();
//    data = $("#id_fy2").val();
//    uid = $("#id_fy3").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/phone_fy',
//        data: { 'cid': cid, 'data': data, 'uid': uid },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}
//
//function phone_sl() {
//    cid = $("#id_sl1").val();
//    uid = $("#id_sl2").val();
//    t_count = $("#id_sl3").val();
//    pos = $("#id_sl4").val();
//    gift = $("#id_sl5").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/phone_sl',
//        data: { 'cid': cid, 'uid': uid, 't_count': t_count, 'pos': pos, 'gift': gift },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}
//
//function phone_sd() {
//    cid = $("#id_sd1").val();
//    uid = $("#id_sd2").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/phone_sd',
//        data: { 'cid': cid, 'uid': uid },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}
//
//function updatestat() {
//    cids = $("#id_name7").val();
//    stat = $("#id_name8").val();
//    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
//    $.ajaxSetup({
//        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
//    });
//    $.ajax({
//        type: "POST",
//        url: '/updatestat',
//        data: { 'cids': cids, 'stat': stat },
//        async: false,
//        success: function(result) {
//            $("div.modal-body").html(result);
//        }
//    });
//}

function texiao(){
//宇宙特效
"use strict";
var canvas = document.getElementById('canvas'),
    ctx = canvas.getContext('2d'),
    w = canvas.width = window.innerWidth,
    h = canvas.height = window.innerHeight,

    hue = 217,
    stars = [],
    count = 0,
    maxStars = 160; //星星数量

var canvas2 = document.createElement('canvas'),
    ctx2 = canvas2.getContext('2d');
canvas2.width = 100;
canvas2.height = 100;
var half = canvas2.width / 2,
    gradient2 = ctx2.createRadialGradient(half, half, 0, half, half, half);
gradient2.addColorStop(0.025, '#CCC');
gradient2.addColorStop(0.1, 'hsl(' + hue + ', 61%, 33%)');
gradient2.addColorStop(0.25, 'hsl(' + hue + ', 64%, 6%)');
gradient2.addColorStop(1, 'transparent');

ctx2.fillStyle = gradient2;
ctx2.beginPath();
ctx2.arc(half, half, half, 0, Math.PI * 2);
ctx2.fill();

// End cache

function random(min, max) {
    if (arguments.length < 2) {
        max = min;
        min = 0;
    }

    if (min > max) {
        var hold = max;
        max = min;
        min = hold;
    }

    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function maxOrbit(x, y) {
    var max = Math.max(x, y),
        diameter = Math.round(Math.sqrt(max * max + max * max));
    return diameter / 2;
    //星星移动范围，值越大范围越小，
}

var Star = function() {

    this.orbitRadius = random(maxOrbit(w, h));
    this.radius = random(60, this.orbitRadius) / 8;
    //星星大小
    this.orbitX = w / 2;
    this.orbitY = h / 2;
    this.timePassed = random(0, maxStars);
    this.speed = random(this.orbitRadius) / 50000;
    //星星移动速度
    this.alpha = random(2, 10) / 10;

    count++;
    stars[count] = this;
}

Star.prototype.draw = function() {
    var x = Math.sin(this.timePassed) * this.orbitRadius + this.orbitX,
        y = Math.cos(this.timePassed) * this.orbitRadius + this.orbitY,
        twinkle = random(10);

    if (twinkle === 1 && this.alpha > 0) {
        this.alpha -= 0.05;
    } else if (twinkle === 2 && this.alpha < 1) {
        this.alpha += 0.05;
    }

    ctx.globalAlpha = this.alpha;
    ctx.drawImage(canvas2, x - this.radius / 2, y - this.radius / 2, this.radius, this.radius);
    this.timePassed += this.speed;
}

for (var i = 0; i < maxStars; i++) {
    new Star();
}

function animation() {
    ctx.globalCompositeOperation = 'source-over';
    ctx.globalAlpha = 0.5; //尾巴
    ctx.fillStyle = 'hsla(' + hue + ', 64%, 6%, 2)';
    ctx.fillRect(0, 0, w, h)

    ctx.globalCompositeOperation = 'lighter';
    for (var i = 1, l = stars.length; i < l; i++) {
        stars[i].draw();
    };

    window.requestAnimationFrame(animation);
}

animation();
}
texiao();
