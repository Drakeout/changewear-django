var dataResult = null;
categoria = 'HM'

$.ajax({
    url: `http://127.0.0.1:8000/api/categoria/HM`,
    dataType: 'json'
}).done((data) => {
    dataResult = data;
    console.log(data)
    dataResult.forEach(element => {
        console.log(element);
    });
});