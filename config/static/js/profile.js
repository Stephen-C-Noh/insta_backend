const tapContainer = document.querySelector('.about');
const flex_Container = document.querySelectorAll('.contents_container');
const taps = document.querySelectorAll('.about > span');

function openCity(e) {
    let elem = e.target;

    if (elem.matches('[class="nick_name"]')) {
        flex_Container[0].classList.add('active');
        flex_Container[1].classList.remove('active');
        taps[0].classList.add('on');
        taps[1].classList.remove('on');
    } else if (elem.matches('[class="book_mark"]')) {
        flex_Container[1].classList.add('active');
        flex_Container[0].classList.remove('active');
        taps[1].classList.add('on');
        taps[0].classList.remove('on');
    }
}

tapContainer.addEventListener('click', openCity);