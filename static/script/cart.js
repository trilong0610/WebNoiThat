console.log("Loadded update-carts")

var updateBtns = document.getElementsByClassName('update-carts')
for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function (){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productID, 'Action:', action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            updateUserOrder(productID, action)
        }
    })
}
function updateUserOrder(productID, action){
    console.log('user is authenticated, sending data..')

    var url = '/updateItem/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productID': productID, 'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        // ------------------Không tự reload lại trang----------------------
        window.location.reload(true)
    })
}

console.log("Loadded permission")
var updatePerms = document.getElementsByClassName('update-permission')
for (i = 0; i < updatePerms.length; i++){
    updatePerms[i].addEventListener('click', function (){
        var user = this.dataset.user
        var permission = this.dataset.permission
        var action = this.dataset.action
        console.log('user:', user, 'permission:', permission, 'action:', action)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            updatePermission(user, permission,action)
        }
    })
}

function updatePermission(user, permission, action){
    console.log('user is authenticated, sending data..')

    var url = '/manager/gains_permission/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'user': user, 'permission':permission, 'action': action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        // ------------------Không tự reload lại trang----------------------
        window.location.reload(false)
    })
}

console.log("Loadded Shipping")
var updateShip = document.getElementsByClassName('update-shipping')
for (i = 0; i < updateShip.length; i++){
    updateShip[i].addEventListener('click', function (){
        var orderid = this.dataset.orderid
        var status = this.dataset.status
        console.log('orderid:', orderid, 'status:', status)
        updateShipping(orderid, status)
    })
}

function updateShipping(orderid, status){
    console.log('user is authenticated, sending data..')

    var url = '/manager/update_shipping/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'orderid': orderid, 'status':status})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        // ------------------Không tự reload lại trang----------------------
        window.location.reload(false)
    })
}
