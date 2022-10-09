const earthSize = 12742
const dateSpan = document.getElementById('date')

function drawBody(radius, canvas, color1='rgb(230, 230, 230)', color2='grey', color3='black') {
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d')

    var circle = new Path2D()
    circle.arc(150, 75, 75*radius/earthSize, 0, 2 * Math.PI)

    // ctx.fillStyle = color
    var gradient = ctx.createRadialGradient(110,90,30, 100,100,90);

    // Add three color stops
    gradient.addColorStop(0, color1);
    gradient.addColorStop(.7, color2);
    gradient.addColorStop(1, color3);

    ctx.fillStyle = gradient;
    ctx.fill(circle)
  }
}

function getDate(epoch) {
  let sec = Math.floor((epoch - Date.now())/1000)
  let min = Math.floor((epoch - Date.now())/60000)
  let hr = Math.floor((epoch - Date.now())/3600000)
  sec - min * 60 < 10 ? sec = '0' + (sec - min * 60).toString() : sec = (sec - min * 60).toString()
  min - hr * 60 < 10 ? min = '0' + (min - hr * 60).toString() : min = (min - hr * 60).toString()
  hr < 10 ? hr = '0' + hr.toString() : hr.toString()
  if (epoch - Date.now() < 0) {
    return 'passed'
  } else {
    return hr + ':' + min + ':' + sec
  }
}

const [todayMonth, todayDate, todayYear] = new Date().toLocaleDateString("en-US").split("/")
apiDate = todayYear + '-' + todayMonth + '-' + todayDate

let approachTime = []
let bodySize = []

var request = new XMLHttpRequest()
const apiKey = '5bbsCyWbCHbQfeQmEEd9e3jYjVwXRh8VGAiINvNr'
const content = document.getElementById('content')

request.open('GET', 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' +
  apiDate + '&end_date=' + apiDate + '&api_key=' + apiKey, true)
request.onload = function () {
  dateSpan.innerHTML = new Date()
  setInterval(() => {
    dateSpan.innerHTML = new Date()
  }, 1000);

  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {
    const asteroidData = data['near_earth_objects']


      for (let i in asteroidData) {
          for (let asteroid in asteroidData[i]) {
            const tr = document.createElement('tr')
            const name = document.createElement('td')
            const size = document.createElement('td')
            const isDangerous = document.createElement('td')
            const closeApproach = document.createElement('td')
            const bodyPicture = document.createElement('td')
            const bodyPictureCanvas = document.createElement('canvas')
            const laser = document.createElement('td')
            const laserButton = document.createElement('button')
            const laserSpan = document.createElement('span')

            const asteroidName = asteroidData[i][asteroid].name
            name.textContent = asteroidName.replace('(', '').replace(')', '')
            tr.appendChild(name)
            size.textContent = asteroidData[i][asteroid]['estimated_diameter'].meters['estimated_diameter_max'].toFixed(1)
            tr.appendChild(size)
            if (asteroidData[i][asteroid].is_potentially_hazardous_asteroid == true) {
              isDangerous.textContent = 'YES'
              isDangerous.style.color = 'red'
            } else {
              isDangerous.textContent = 'NO'
            }
            tr.appendChild(isDangerous)
            closeApproach.textContent = getDate(asteroidData[i][asteroid]['close_approach_data']['0']
            ['epoch_date_close_approach'])
            closeApproach.setAttribute('class', 'countdown')
            approachTime.push(asteroidData[i][asteroid]['close_approach_data']['0']
            ['epoch_date_close_approach'])
            tr.appendChild(closeApproach)
            drawBody(parseFloat(size.textContent) * 15, bodyPictureCanvas)
            bodySize.push(parseFloat(size.textContent) * 15)
            bodyPicture.appendChild(bodyPictureCanvas)
            tr.appendChild(bodyPicture)
            laserButton.textContent = 'Laser it!'
            laserButton.setAttribute('class', 'laser')
            laser.appendChild(laserButton)
            laserSpan.textContent = 'Access denied'
            laserSpan.setAttribute('class', 'joke')
            laser.appendChild(laserSpan)
            tr.appendChild(laser)

            content.appendChild(tr)
          }
      }

    const countdown = document.getElementsByClassName('countdown')
    setInterval(() => {
      for (let i = 0; i < approachTime.length; i++ ){
        countdown[i].innerHTML = getDate(approachTime[i])
        if (getDate(approachTime[i]) != 'passed' && countdown[i].previousElementSibling.innerHTML == 'YES') {
          countdown[i].style.color = 'red'
        }
      }
    }, 1000);

  } else {
    console.log('error')
  }

  const laserButtons = document.getElementsByClassName('laser')
  for (let b of laserButtons) {
    b.addEventListener('click', function (e) {
      this.style.display = 'none'
      this.nextSibling.style.display = 'inline'
    })
  }

  const icons = document.querySelectorAll('canvas')
  setInterval(() => {
    for (i = 0; i < icons.length; ++i) {
      const rColor = Math.random()*255
      const rgbColor1 = 'rgb(' + (rColor*1.3).toFixed(2) + ', ' + (rColor*1.3).toFixed(2) + ', ' + (rColor*1.3).toFixed(2) + ')'
      const rgbColor2 = 'rgb(' + (rColor/4).toFixed(2) + ', ' + (rColor/4).toFixed(2) + ', ' + (rColor/4).toFixed(2) + ')'
      const rgbColor3 = 'rgb(' + (rColor/10).toFixed(2) + ', ' + (rColor/10).toFixed(2) + ', ' + (rColor/10).toFixed(2) + ')'
      console.log()
      drawBody(bodySize[i], icons[i], rgbColor1, rgbColor2, rgbColor3)

    }
  }, Math.random()*500+1000);

}

request.send()
