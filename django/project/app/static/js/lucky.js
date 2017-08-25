function set_money() {
    id_name = $("#id_name1").val();
    id_xd = $("#id_xd").val();
    id_mb = $("#id_mb").val();
    id_md = $("#id_md").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/set_money',
        data: { 'id_name': id_name, 'id_xd': id_xd, 'id_mb': id_mb, 'id_md': id_md },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function bd_sj() {
    id_name = $("#id_name2").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/bd_sj',
        data: { 'id_name': id_name },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function zc() {
    id_name = $("#id_name3").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/zc',
        data: { 'id_name': id_name },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function sq_zb() {
    id_name = $("#id_name4").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/sq_zb',
        data: { 'id_name': id_name },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function update_stream() {
    room_number_online = $("#id_name5").val();
    room_number_offine = $("#id_name6").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/update_stream',
        data: { 'room_number_online': room_number_online, 'room_number_offine': room_number_offine },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function phone_fy() {
    cid = $("#id_fy1").val();
    data = $("#id_fy2").val();
    uid = $("#id_fy3").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/phone_fy',
        data: { 'cid': cid, 'data': data, 'uid': uid },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function phone_sl() {
    cid = $("#id_sl1").val();
    uid = $("#id_sl2").val();
    t_count = $("#id_sl3").val();
    pos = $("#id_sl4").val();
    gift = $("#id_sl5").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/phone_sl',
        data: { 'cid': cid, 'uid': uid, 't_count': t_count, 'pos': pos, 'gift': gift },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function phone_sd() {
    cid = $("#id_sd1").val();
    uid = $("#id_sd2").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/phone_sd',
        data: { 'cid': cid, 'uid': uid },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}

function updatestat() {
    cids = $("#id_name7").val();
    stat = $("#id_name8").val();
    csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({
        data: { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
    });
    $.ajax({
        type: "POST",
        url: '/updatestat',
        data: { 'cids': cids, 'stat': stat },
        async: false,
        success: function(result) {
            $("div.modal-body").html(result);
        }
    });
}
