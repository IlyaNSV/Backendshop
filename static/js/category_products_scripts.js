window.onload = function () {
    console.log('DOM loaded');

    $('.noUi-handle.noUi-handle-lower').on('mouseup', null,function (event) {
        let lowerprice = parseInt($(event.target).attr('aria-valuetext'), 10);
        console.log(lowerprice)
        $.ajax({
            url: 'filter/l_price/'+ lowerprice + '/',
            success: function (data) {
                console.log(data)
                $('.basket_list').html(data.result);
            }
        });
    })
};