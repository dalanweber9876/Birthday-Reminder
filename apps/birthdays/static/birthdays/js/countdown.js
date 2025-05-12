document.addEventListener("DOMContentLoaded", () => {
  console.log("Birthday countdown script loaded");
  document.querySelectorAll("[data-birthday]").forEach((el) => {
    const dateStr = el.dataset.birthday;
    const birthdayDate = new Date(dateStr + "T00:00:00");

    function updateCountdown() {
      const now = new Date();
      let nextBirthday = new Date(
        now.getFullYear(),
        birthdayDate.getMonth(),
        birthdayDate.getDate()
      );

      if (nextBirthday < now) {
        nextBirthday.setFullYear(now.getFullYear() + 1);
      }

      const diff = nextBirthday - now;
      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
      const minutes = Math.floor((diff / (1000 * 60)) % 60);
      const seconds = Math.floor((diff / 1000) % 60);

      el.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s left`;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
  });
});
