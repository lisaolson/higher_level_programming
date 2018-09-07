$.get('https://swapi.co/api/films/?format=json', function(data, textStatus)
{
        for (let i = 0; i < data.results.length; i++)
    {
            console.log(data.results[i].title);
        $('#list_movies').append('<li>' + data.results[i].title + '</li>');
    }
});
