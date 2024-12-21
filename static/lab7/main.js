function fillFilmList() {
    fetch('/lab7/rest-api/films/')
    .then(function (response) {
        return response.json();
    })
    .then(function (films) {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        for(let i = 0; i < films.length; i++) { // Исправлено на films.length
            let tr = document.createElement('tr');

            let tdTitle = document.createElement('td');
            let tdTitleRus = document.createElement('td');
            let tdTitleYear = document.createElement('td');
            let tdActions = document.createElement('td');

            tdTitle.innerText = films[i].title === films[i].title_ru ? '' : films[i].title;
            tdTitleRus.innerText = films[i].title_ru;
            tdTitleYear.innerText = films[i].year;

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.onclick = function() {
                // Здесь можно добавить логику редактирования
                alert('Редактирование фильма: ' + films[i].title);
            };

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteFilm(i, films[i].title_ru);
            };

            tdActions.appendChild(editButton);
            tdActions.appendChild(delButton);

            tr.appendChild(tdTitle);
            tr.appendChild(tdTitleRus);
            tr.appendChild(tdTitleYear);
            tr.appendChild(tdActions);

            tbody.appendChild(tr);
        }
    })
    .catch(function (error) {
        console.error('Ошибка:', error);
    });
}

function deleteFilm(id, title) {
    if(! confirm(`Вы точно хотите удалить фильм "${title}" ?`))
        return;

    fetch(`/lab7/rest-api/films/${id}`, {method: 'DELETE'})
        .then(function() {
            fillFilmList();
        });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}
function addFilm() {
    showModal();
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

function sendFilm() {
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value
    }

    const url = `/lab7/rest-api/films/`;
    const method = 'POST';

    fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(film)
    })
    .then(function() {
        fillFilmList();
        hideModal();
    })
}