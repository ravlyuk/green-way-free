function day() {
    const title = document.getElementById('title');
    title.innerHTML = `Передбачити день`;
    const raceview = document.getElementById('page-content');
    raceview.innerHTML = '';

    const race = document.createElement("div");
    race.classList.add("race");
    raceview.appendChild(race);

    race.innerHTML = `    
        <div class="container">
            <div class="col-md-6 offset-md-3 col-sm-12">
                <h2 class="text-center mb-4">Який день тижня для цієї дати?</h2>
                <h2 class="text-center" id="date"></h2>
                <form class="text-center" onsubmit="return checkDay(event)">
                    <div class="form-group">
                        <label for="day">Виберіть день тижня:</label>
                        <select class="form-control" id="day">
                            <option value="Sunday">Неділя</option>
                            <option value="Monday">Понеділок</option>
                            <option value="Tuesday">Вівторок</option>
                            <option value="Wednesday">Середа</option>
                            <option value="Thursday">Четвер</option>
                            <option value="Friday">Пʼятниця</option>
                            <option value="Saturday">Субота</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-success mt-4">Перевірити</button>
                </form>
                <p class="text-center mt-4 font-weight-bold" id="result"></p>
                <div class="text-center">   
                    <button type="button" class="btn-secondary btn-light" onclick="setRandomDate()">Нова дата</button>
                </div>
            </div>
        </div> 
    `;

    setRandomDate()
}

// Get a random date
function getRandomDate() {
    let start = new Date(-11676096000000); // 01/01/1600
    let end = new Date();
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}


function setRandomDate() {
    document.getElementById("date").textContent = getRandomDate().toDateString().split(' ').slice(1).join(' ');
    document.getElementById("result").textContent = "";
    document.getElementById("result").classList.remove("text-danger");
}

// Check the selected day against the correct day of the week for the random date
function checkDay(event) {
    event.preventDefault();
    let date = new Date(document.getElementById("date").textContent);
    let day = document.getElementById("day").value;
    let correctDay = date.toLocaleString('en-US', {weekday: 'long'});
    if (day === correctDay) {
        document.getElementById("result").textContent = "Правильно";
        document.getElementById("result").classList.remove("text-danger");
        document.getElementById("result").classList.add("text-success");
    } else {
        document.getElementById("result").textContent = "Не правильно";
        document.getElementById("result").classList.remove("text-success");
        document.getElementById("result").classList.add("text-danger");
    }
}

