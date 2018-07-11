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
            $.ajax({
                type: "POST",
                url: url,
                data: data,
                async: false,
                success: function(result) {
                    result = JSON.parse(result);
                    if(result.code == 100){
                         $('.btn-primary').addClass('hidden');
                         $('.modal-footer a').removeClass('hidden');
                    }else{
                        $('.btn-primary').removeClass('hidden');
                        $('.modal-footer a').addClass('hidden');
                    }
                    $('.modal-body').text(result.msg);
                    $('#myModal').modal('show');
                    if (result.uid != undefined){
                        $('.uid').val(result.uid);
                    };
                    }
            });
            return;
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
            data = $("#find_uid_form").serialize();
            break;
        case 'init_fans':
            url = '/new_web/init_fans';
            data = $("#init_fans_form").serialize();
            break;
        case 'update_password':
            url = '/new_web/update_password';
            data = $("#update_password_form").serialize();
            break;
        case 'test_fun':
            url = '/new_web/test_fun';
            data = '';
            break;
        case 'init_active':
            url = '/new_web/init_active';
            data = '';
            break;
        case 'add_mobile_yzm':
            url = '/new_web/add_mobile_yzm';
            data = $("#add_mobile_yzm_form").serialize();
            break;
        case 'mn_login':
            url = '/new_web/mn_login';
            data = $("#mn_login_form").serialize();
            $.ajax({
                type: "POST",
                url: url,
                data: data,
                async: false,
                success: function(result) {
                    window.open('http://qa.new.huomaotv.com.cn/1');
                    }
                });
                return;
    }
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        async: false,
        success: function(result) {
            $('.btn-primary').removeClass('hidden');
            $('.modal-footer a').addClass('hidden');
            $('.modal-body').text(result.msg);
            $('#myModal').modal('show');
            if (result.uid != undefined){
                $('.uid').val(result.uid);
            };
//            setTimeout(function(){$("#myModal").modal("hide")},20000);
        }
    });

}




