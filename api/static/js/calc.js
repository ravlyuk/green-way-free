function calc() {
    const title = document.getElementById('title');
    title.innerHTML = `Калькулятор відсотків числа X від числа Y`;
    const raceview = document.getElementById('page-content');
    raceview.innerHTML = '';

    const race = document.createElement("div");
    race.classList.add("race");
    raceview.appendChild(race);

    race.innerHTML = `
    <div class="container">
            <div class="col-md-6 offset-md-3 col-sm-12">
                <form>
                    <input type="number" id="number" placeholder="Введіть число 1">
                    <input type="number" id="percentage" placeholder="Введіть число 2">
                    <button type="button" class="btn" onclick="calculate()">Розрахувати</button>
                </form>
                <p class="result" id="result"></p>
            </div>
        </div>
    `;
}


function calculate() {
    let number = document.getElementById("number").value;
    let percentage = document.getElementById("percentage").value;
    let result = ((number / percentage) * 100).toFixed(2);
    document.getElementById("result").innerHTML = "Result: " + result + "%";
}

document.getElementsByTagName("input").oninput = function (event) {
    this.value = this.value.replace(/[^0-9.,]/g, '').replace(/(\..*?)\..*/g, '$1');
};