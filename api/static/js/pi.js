function pi() {
    const title = document.getElementById('title');
    title.innerHTML = `Pi number`;
    const raceview = document.getElementById('page-content');
    raceview.innerHTML = '';
    const race = document.createElement("div");
    race.classList.add("race");
    raceview.appendChild(race);

    race.innerHTML = `
        <div class="col-md-6 offset-md-3 col-sm-12">
            <div class="card p-4">
                <h1 class="text-center mb-4 pi-title">PI Number Checker</h1>
                <form autocomplete="off">
                    <div class="form-group">
                        <label class="pi-title" for="piNumber">Enter the first 100 digits of PI:</label>
                        <input type="text" class="form-control form-control-lg" id="piNumber" name="piNumber" size="100"
                               required oninput="this.value = this.value.replace(/[^0-9.,]/g, '').replace(/(\\..*?)\\..*/g, '$1');">
                    </div>
                    <button type="submit" class="btn btn-success btn-lg btn-block" >Submit</button>
                </form>
                <div id="result" class="mt-4 text-center"></div>
            </div>
        </div>
    `;


    const result = document.getElementById("result");

    document.addEventListener('submit', (event) => {
        event.preventDefault();
        const piNumber = event.target.elements.piNumber.value.replace(',', '.');
        const piRegex = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";

        if (piNumber === piRegex) {
            result.innerHTML = 'Correct';
            result.classList.add('text-success');
            result.classList.remove('text-danger');
        } else {
            result.innerHTML = 'Mistake';
            result.classList.add('text-danger');
            result.classList.remove('text-success');
        }
    })
}

document.getElementsByTagName("input").oninput = function (event) {
    this.value = this.value.replace(/[^0-9.,]/g, '').replace(/(\..*?)\..*/g, '$1');
};