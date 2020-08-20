window.onload = function () {
    console.log('DOM loaded');

    $('.noUi-handle.noUi-handle-lower').on('mouseup', null,function (event) {
        let lowerprice = parseInt($(event.target).attr('aria-valuetext'), 10);
        console.log(lowerprice)
        $.ajax({
            url: 'filter/price/lower/' + lowerprice + '/',
            success: function (data) {
                console.log(data)
                $('.lattest-product-area.pb-40.category-list').html(data.result);
            }
        });
    });
    $('.noUi-handle.noUi-handle-upper').on('mouseup', null,function (event) {
        let upperprice = parseInt($(event.target).attr('aria-valuetext'), 10);
        console.log(upperprice)
        $.ajax({
            url: 'filter/price/upper/' + upperprice + '/',
            success: function (data) {
                console.log(data)
                $('.lattest-product-area.pb-40.category-list').html(data.result);
            }
        });
    });
    $('.filter-list').on('click', 'input[type=radio]',function (event) {
        let brand = $(event.target).attr('id');
        console.log(brand)
        $.ajax({
            url: 'filter/brand/' + brand + '/',
            success: function (data) {
                console.log(data)
                $('.lattest-product-area.pb-40.category-list').html(data.result);
            }
        });
    })
};