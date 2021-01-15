console.log("Loadded update-carts")
//---------------Tang giam so luong san pham trong gio hang 1 don vi----------------
var updateBtns = document.getElementsByClassName('update-carts')
for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function (){
        var sizeProductID = this.dataset.sizeproduct
        var action = this.dataset.action
        console.log('sizeProductID:', sizeProductID, 'Action:', action)
        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            updateUserOrder(sizeProductID, action)
        }
    })
}
function updateUserOrder(sizeProductID, action){
    console.log('user is authenticated, sending data..')

    var url = '/updateItem/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'sizeProductID': sizeProductID, 'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        if(data["outStock"]){
        alert("Sản phẩm trong kho không đủ, vui lòng kiểm tra lại" + "\nSố lượng còn lại: " + data["amount_product"])
        }
        // ------------------Không tự reload lại trang----------------------
        window.location.reload(true)
    })
}


console.log("Loadded add-item-carts")
//Tang giam so luong san pham trong gio hang theo so luong nhap vao
var addToCartBtns = document.getElementsByClassName('add-item-carts')
for (i = 0; i < addToCartBtns.length; i++){
    addToCartBtns[i].addEventListener('click', function (){
        var quantity = document.getElementById("id_quantity_single_product").value;
        var sizeProductID = document.getElementById("id_size_single_product").value;
        console.log('sizeProductID:', sizeProductID, 'quantity', quantity)
        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            addItemToCart(sizeProductID, quantity)
        }
    })
}
function addItemToCart(sizeProductID, quantity){
    console.log('user is authenticated, sending data..')

    var url = '/addItemToCart/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'sizeProductID': sizeProductID, 'quantity':quantity})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        if(data["outStock"]){
        alert("Sản phẩm trong kho không đủ, vui lòng kiểm tra lại" + "\nSố lượng còn lại: " + data["amount_product"])
    }
        console.log('data:', data)
        // ------------------Không tự reload lại trang----------------------
        window.location.reload(true)
    })
}


//auto Tang giam so luong san pham trong gio hang theo so luong nhap vao input trong manager

console.log("Loadded update-item-order")
var updateToOrderBtns = document.getElementsByClassName('update-item-order')
for (i = 0; i < updateToOrderBtns.length; i++){
    updateToOrderBtns[i].addEventListener('change', function (){
        var orderID = this.dataset.order
        var sizeProductID = this.dataset.sizeproduct
        var quantity = document.getElementById("quantity_product_order_"+sizeProductID).value;
        console.log('productID:', sizeProductID, 'quantity', quantity)
        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            updateItemToOrder(orderID,sizeProductID, quantity)
        }
    })
}
function updateItemToOrder(orderID,sizeProductID, quantity){
console.log('user is authenticated, sending data..')

var url = '/order/editOrder/'

fetch(url,{
    method: 'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'orderID': orderID,'sizeProductID': sizeProductID, 'quantity':quantity})
})
.then((response) => {
    return response.json();
})
.then((data) => {
    if(data["outStock"]){
        alert("Sản phẩm trong kho không đủ, vui lòng kiểm tra lại" + "\nSố lượng còn lại: " + data["amount_product"])
    }


    console.log('data:', data)
    // ------------------Không tự reload lại trang----------------------
    window.location.reload(true)
})
}


//auto Tang giam so luong san pham trong gio hang theo so luong nhap vao input trong cart
console.log("Loadded update-item-carts")
var updateToCartBtns = document.getElementsByClassName('update-item-carts')
for (i = 0; i < updateToCartBtns.length; i++){
    updateToCartBtns[i].addEventListener('keyup', function (){
        var sizeProductID = this.dataset.sizeproduct
        var quantity = document.getElementById("quantity_product_cart_"+sizeProductID).value;
        console.log('productID:', sizeProductID, 'quantity', quantity)
        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            updateItemToCart(sizeProductID, quantity)

        }
    })
}
function updateItemToCart(sizeProductID, quantity){
console.log('user is authenticated, sending data..')

var url = '/cart/editItemQuantity/'

fetch(url,{
    method: 'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'sizeProductID': sizeProductID, 'quantity':quantity})
})
.then((response) => {
    return response.json();
})
.then((data) => {
    if(data["outStock"]){
        alert("Sản phẩm trong kho không đủ, vui lòng kiểm tra lại" + "\nSố lượng còn lại: " + data["amount_product"])
    }
    console.log('data:', data)
    // ------------------Không tự reload lại trang----------------------
    window.location.reload(true)
})
}


//---------------xoa san pham trong gio hang ---------------
console.log("Loadded remove-item-carts")
var removeToCartBtns = document.getElementsByClassName('remove-item-carts')
for (i = 0; i < removeToCartBtns.length; i++){
    removeToCartBtns[i].addEventListener('click', function (){
        var sizeproductID = this.dataset.sizeproduct
        console.log('productID:', sizeproductID)
        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            removeItemToCart(sizeproductID)
        }
    })
}
function removeItemToCart(sizeproductID){
    console.log('user is authenticated, sending data..')

    var url = '/deleteProductCart/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'sizeproductID': sizeproductID})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        window.location.reload(true)
    })
}


//---------------Sua thong tin ca nhan---------------
console.log("Loadded change-info-user")
var InfoUser = document.getElementsByClassName('change-info-user')
for (i = 0; i < InfoUser.length; i++){
    InfoUser[i].addEventListener('click', function (){
        var firstName = document.getElementById("firstName").value;
        var lastName = document.getElementById("lastName").value;
        var email = document.getElementById("email").value;
        var phone = document.getElementById("phone").value;
        var province = document.getElementById("province").value;
        var district = document.getElementById("district").value;
        var wards = document.getElementById("wards").value;
        var address = document.getElementById("address").value;
        console.log('firstName:', firstName, 'lastName:', lastName, 'email:', email)
        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log("user is not authenticated")
        }
        else {
            changeInfoUser(firstName, lastName, email, phone, province, district, wards, address)
        }
    })
}
function changeInfoUser(firstName, lastName, email, phone, province, district, wards, address){
    console.log('user is authenticated, sending data..')
    var url = '/user/changeInfoUser/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'firstName': firstName, 'lastName':lastName, 'email':email, 'phone':phone, 'province':province, 'district':district, 'wards':wards, 'address':address})
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

//-----------------------------------------------------------


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

    var url = '/manager/gainsPermission/'

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
        alert("Complete " + data["action"] + " permission " + data["permission"] )
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
//---------------Tìm sản phẩm---------------
console.log("Loadded search")
var keySearch = document.getElementsByClassName('search-product')
for (i = 0; i < keySearch.length; i++){
    keySearch[i].addEventListener('click', function (){
        var key = this.dataset.key
        console.log('key:', key)
        searchProduct(key)
    })
}
function searchProduct(key){
    console.log('user is authenticated, sending data..')

    var url = '/search/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'key': key})
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