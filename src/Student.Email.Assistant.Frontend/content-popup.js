const popupSelector = ".I5";

const titleClass = "az6";
const titleInputSelector = `form.bAs .${titleClass}`;
const contentInputClass = "Au";
const contentInputSelector = `.Ap .${contentInputClass}`;
const emailInputClass = "az9";
const emailInputSelector = `.${emailInputClass} span`;

function shouldRerender(mutations) {
  return mutations.some(
    (mutation) =>
      mutation.target.classList.contains(titleClass) ||
      mutation.target.classList.contains(contentInputClass) ||
      mutation.target.classList.contains(emailInputClass)
  );
}

function getPopup(popup) {
  const contentInput = popup.querySelector(contentInputSelector);
  const titleInput = popup.querySelector(titleInputSelector);

  return {
    contentInput,
    titleInput,
    emailAccessor: () => {
      const input = popup.querySelector(emailInputSelector);
      return input?.getAttribute("email");
    },
  };
}

function getPopups() {
  const popups = document.querySelectorAll(popupSelector);
  return popups.values().map(getPopup);
}