// cars-json
const carForm = document.getElementById('car-form')
const carsDataBox = document.getElementById('cars-data-box')
const carInput = document.getElementById('cars')
const modelsDataBox = document.getElementById('models-data-box')
const modelInput = document.getElementById('models')

const modelText = document.getElementById('model-text')
const carText = document.getElementById('car-text')

const btnBox = document.getElementById('btn-box')
const alertBox = document.getElementById('alert-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

$.ajax({
    type: "GET",
    url: '/cars-json/',
    success: function (response) {
        console.log(response.data)
        const carsData = response.data
        carsData.map(item => {
            const option = document.createElement('div')
            option.textContent = item.name
            option.setAttribute('class', 'item')
            option.setAttribute('data-value', item.name)
            carsDataBox.appendChild(option)
        })
    },
    error: function (error) {
        console.log(error)
    }
})

carInput.addEventListener('change', e => {
    console.log(e.target.value)
    const selectedCar = e.target.value
    alertBox.innerHTML = ''
    modelsDataBox.innerHTML = ""
    modelText.textContent = "Choose a model"
    modelText.classList.add("default")
    btnBox.classList.add('not-visible')


    $.ajax({
        type: 'GET',
        url: `models-json/${selectedCar}/`,
        success: function (response) {
            console.log(response.data)
            const modelsData = response.data
            modelsData.map(item => {
                const option = document.createElement('div')
                option.textContent = item.name
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.name)
                modelsDataBox.appendChild(option)
            })

            modelInput.addEventListener('change', e => {
                btnBox.classList.remove('not-visible')
            })

        },
        error: function (error) {
            console.log(error)
        }
    })

})

carForm.addEventListener('submit', e => {
    e.preventDefault()
    $.ajax({
        type: 'POST',
        url: '/create/',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'car': carText.textContent,
            'model': modelText.textContent,
        },
        success: function (response) {
            console.log(response)
            alertBox.innerHTML = '<div class="ui positive message">\n' +
                '  <div class="header">\n' +
                '    You are eligible for a reward\n' +
                '  </div>\n' +
                '  <p>Your order is succesfully been placed</p>\n' +
                '</div>'

        },
        error: function (error) {
            console.log(error)
            alertBox.innerHTML = '<div class="ui negative message">\n' +
                '  <div class="header">\n' +
                '    this is fucked up\n' +
                '  </div>\n' +
                '  <p>Something went wrong</p>\n' +
                '</div>'
        }
    })
})