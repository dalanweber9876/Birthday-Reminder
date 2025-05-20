const menu = document.querySelector(".hamburger-menu");
const navigation = document.querySelector(".navigation");

function toggleMenu() {
  if (menu.classList.contains("open")) {
    menu.classList.remove("open");
    navigation.classList.remove("open");
  } else {
    menu.classList.add("open");
    navigation.classList.add("open");
  }
}
