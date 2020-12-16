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