$(document).ready(function(){
    categoria = document.getElementById('categoria').innerHTML;

    
    if (categoria == 'Mujer'){
        id = 'MJ'
    } else if (categoria == 'Hombre'){
        id = 'HM'
    } else if (categoria == 'Niños'){
        id = 'NN'
    }

    var dataResult = null;

    $.ajax({
        url: `http://127.0.0.1:8000/api/categoria/${id}`,
        dataType: 'json',
        
    }).done((data) => {
        dataResult = data;
        mostrarProductos(dataResult)
    });

    const tarjetaProducto = (titulo, imgs, precio, description, id) => {
        let html = `
            <div class="card border rounded mt-2 shadow-sm">
                <img src="${imgs}" class="card-img-top"/>
                <div class="card-body">
                    <h5 class="card-title">${titulo}</h5>
                </div>
                <div class="card-footer mx-auto">
                    <p class="card-text ">$ ${precio}</p>
                </div>    
            </div>
        `;
        let card = document.createElement('div');
        $(card).html(html);
        $(card).addClass('col');
        $(card).attr('id', id);
        $(card).click(() => {
            window.location.href = `http://127.0.0.1:8000/producto/${id}`;
        });

        return card;
    };

    const mostrarProductos = (dataResult) => {
        $("#productos").empty();
        dataResult.map(producto => {
            $("#productos").append(
                tarjetaProducto(
                    producto.titulo,
                    producto.imagen,
                    producto.precio,
                    producto.descripcion,
                    producto.id
                )
            );
        });
    };
})
    
