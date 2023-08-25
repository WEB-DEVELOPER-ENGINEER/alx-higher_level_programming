// a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $.each(data.results, function (index, value) {
        $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
    });
});
