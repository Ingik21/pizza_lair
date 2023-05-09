


console.log('cart.js is working')



var updateBtns = document.getElementsByClassName('update-cart')

/* Add pizzas to cart */

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function() {
        var pizzaId = this.dataset.pizza
        var action = this.dataset.action
        console.log('pizzaId:', pizzaId, 'Action:', action)
            console.log('USER', user)
        if (user === 'AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            updateUserOrder(pizzaId, action)
        }
    })
}

function updateUserOrder(pizzaId, action) {
    console.log('User is logged in, sending data...')
    var url = '/cart/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'pizzaId': pizzaId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}






/* Add offers to cart */

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function() {
        var offerId = this.dataset.offer
        var action = this.dataset.action
        console.log('offerId:', offerId, 'Action:', action)
            console.log('USER', user)
        if (user === 'AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            updateUserOrderOffer(offerId, action)
        }
    })
}

function updateUserOrderOffer(offerId, action) {
    console.log('User is logged in, sending data...')
    var url = '/cart/update_item_offer'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'offerId': offerId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}

