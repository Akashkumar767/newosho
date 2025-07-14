const pics = ["static/images/os.jpg","static/images/osho.jpg","static/images/osho4.jpg",];
let i=0;
window.onload = function() {
    setInterval(() => {
        i=(i + 1) % pics.length;
        document.getElementById("right").src = pics[i];
    },4000);
};
let likes = 0, views = 0;

  function like() {
    likes++;
    document.getElementById('like-count').innerText = likes;
  }

  function view() {
    views++;
    document.getElementById('view-count').innerText = views;
  }

  function subscribe() {
    alert("Thanks for subscribing!");
  }
  function search() {
    let query = document.getElementById('search').value;
    alert("You searched for: " + query);
  }
  function toggleMenu() {
    const menu = document.getElementById('menu');
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block';
  }
  function redirectToindex() {
    window.location.href = "index.html";
  }





