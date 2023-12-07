console.log("ll");

const url = window.location.href
const search = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultSerach = document.getElementById('result-serach')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const sendInputSearch = (movie) => {
    $.ajax({
        type: "POST",
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'movie': movie,
        },
        success: (response) => {
            console.log(response.daa);
            data = response.data;
            if (searchInput.value.length < 1) {
                resultSerach.classList.add('hidden-visible')
            }
            if (Array.isArray(data)) {
                resultSerach.innerHTML = ""
                data.forEach(movie => {
                    resultSerach.innerHTML += `
                    <a
                    <a class="item" href="movie/${movie.PRIMARY_KEY}">
        <div class="cardItemSearch">
            <div class="imageContainer">
                <img class="imageCategory" src="media/${movie.image}" alt="Movie Image">
            </div>
            <div class="movieDetails">
                <h3 class="movieTitle">${movie.title}</h3>
                <p class="movieDescription">${movie.description}</p>
            </div>
        </div>
    </a>`;
                });
            }
            else {
                if (searchInput.value.length > 0) {
                    resultSerach.innerHTML = `<b>${data}<b>`
                }
                // else{
                //     resultSerach.classList.add('hidden-visible')
                // }
            }
        },
        error: (error) => {
            console.log(error);
        }
    })
}

searchInput.addEventListener('keyup', e => {
    console.log(e.target.value);
    if (resultSerach.classList.contains('hidden-visible')) {
        resultSerach.classList.remove('hidden-visible')
    }

    sendInputSearch(e.target.value);
})
console.log(csrf);