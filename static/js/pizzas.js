$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/pizza?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="wellPizza">
                                <a href="/pizza/${d.id}">
                                    <img class="pizzaImage" src="${d.firstImage}" alt=""/>
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                    <p>${d.base_price} ISK</p>
                                </a>
                            </div>`
                });
                $('.pizzas').html(newHtml.join(''));
                $('#search-box').val('');
        },
        error: function (xhr, status, error) {
                //TODO: Show toastr error
                console.error(error);
            }
        });
    });
});


document.getElementById("order-by-price").addEventListener("click", function () {
  fetch('/?order_by=base_price')
    .then(response => response.text())
    .then(data => {
      document.getElementsByTagName("body")[0].innerHTML = data;
    });
});

document.getElementById("order-by-name").addEventListener("click", function () {
  fetch('/?order_by=name')
    .then(response => response.text())
    .then(data => {
      document.getElementsByTagName("body")[0].innerHTML = data;
    });
});

