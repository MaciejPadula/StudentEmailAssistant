const popupSelector = ".I5";

const titleClass = "az6";
const titleInputSelector = `form.bAs .${titleClass}`;
const contentInputClass = "Au";
const contentInputSelector = `.Ap .${contentInputClass}`;

function shouldRerender(mutations) {
  return mutations.some(
    (mutation) =>
      mutation.target.classList.contains(titleClass) ||
      mutation.target.classList.contains(contentInputClass)
  );
}

function getPopup(popup) {
  const contentInput = popup.querySelector(contentInputSelector);
  const titleInput = popup.querySelector(titleInputSelector);

  return {
    contentInput,
    titleInput,
  };
}

function getPopups() {
  const popups = document.querySelectorAll(popupSelector);
  return popups.values().map(getPopup);
}