var updateButtons = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function(){
        var productoId = this.dataset.producto
        var action = this.dataset.action
        console.log(productoId, action)

        if(user === 'AnonymousUser'){
            console.log('Sin cuenta registrada');
        }else{
            updateUserCompra(productoId, action)   
        }
    })
} 

function updateUserCompra(productoId, action){
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productoId, 'action': action})
    })

    .then((response)=>{
        return response.json()
    })
    
    .then((data)=>{
        console.log('data:', data);
        location.reload();
    })
}