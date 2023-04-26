function day() {
    const title = document.getElementById('title');
    title.innerHTML = `Predict day`;
    const raceview = document.getElementById('page-content');
    raceview.innerHTML = '';

    const race = document.createElement("div");
    race.classList.add("race");
    raceview.appendChild(race);

    race.innerHTML = `    
        <div class="container">
            <div class="col-md-6 offset-md-3 col-sm-12">
                <h2 class="text-center mb-4">What day of the week is this date?</h2>
                <h2 class="text-center" id="date"></h2>
                <form class="text-center" onsubmit="return checkDay(event)">
                    <div class="form-group">
                        <label for="day">Select the day of the week:</label>
                        <select class="form-control" id="day">
                            <option value="Sunday">Sunday</option>
                            <option value="Monday">Monday</option>
                            <option value="Tuesday">Tuesday</option>
                            <option value="Wednesday">Wednesday</option>
                            <option value="Thursday">Thursday</option>
                            <option value="Friday">Friday</option>
                            <option value="Saturday">Saturday</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-success mt-4">Check Answer</button>
                </form>
                <p class="text-center mt-4 font-weight-bold" id="result"></p>
                <div class="text-center">   
                    <button type="button" class="btn-secondary btn-light" onclick="setRandomDate()">New date</button>
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
        document.getElementById("result").textContent = "Correct";
        document.getElementById("result").classList.remove("text-danger");
        document.getElementById("result").classList.add("text-success");
    } else {
        document.getElementById("result").textContent = "Wrong";
        document.getElementById("result").classList.remove("text-success");
        document.getElementById("result").classList.add("text-danger");
    }
}

