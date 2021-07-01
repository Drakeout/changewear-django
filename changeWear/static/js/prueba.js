var dataResult = null;

$.ajax({
    
    url: `http://127.0.0.1:8000/api/productos`,
    dataType: 'json'
}).done((data) => {
    dataResult = data;
    dataResult.forEach(element => {
        console.log(element.precio);
    });
});