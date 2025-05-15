const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

fetch(setTimezoneUrl, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-CSRFToken": csrfToken,
  },
  body: JSON.stringify({ timezone: tz }),
});
