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
            url = '/new_web/register';
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
        case 'test_fun':
            url = '/new_web/test_fun'
            data = ''
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
//            setTimeout(function(){$("#myModal").modal("hide")},20000);
        }
    });
}

