
MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

const apiUrl = "http://127.0.0.1:8080";

const link = document.createElement('link');
link.rel = 'stylesheet';
link.href = 'https://fonts.googleapis.com/icon?family=Material+Icons';
document.head.appendChild(link);

function addGenerateTitleButton(titleInput, contentInput) {
  const generateTitleButtonClass = "generate-title";
  const inputValueContainer = titleInput.querySelector("input");
  const contentInputValueContainer = contentInput.querySelector(".aO7 div");
  const btn = createIconButton(
    "psychology",
    generateTitleButtonClass,
    async () => {
      const response = await fetch(`${apiUrl}/api/generate-title`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "email_content": contentInputValueContainer.innerHTML
        }),
      });
      const popupResult = openDialog(await response.json());

      if (popupResult.ok) {
        inputValueContainer.value = popupResult.result;
      }
    }
  );
  btn.style.position = "absolute";
  btn.style.top = "0";
  btn.style.right = "0";

  tryAppendButton(titleInput, generateTitleButtonClass, btn);
}

function addImproveEmailButton(contentInput, emailAccessor) {
  const improveContentButtonClass = "improve-content";
  const contentInputValueContainer = contentInput.querySelector(".aO7 div");
  const btn = createIconButton(
    "auto_fix_high",
    improveContentButtonClass,
    async () => {
      const response = await fetch(`${apiUrl}/api/improve-content`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "receiver_email": emailAccessor(),
          "email_content": contentInputValueContainer.innerHTML
        }),
      });
      const popupResult = openDialog(await response.json());

      if (popupResult.ok) {
        contentInputValueContainer.innerHTML = popupResult.result;
      }
    }
  );
  btn.style.position = "absolute";
  btn.style.top = "0";
  btn.style.right = "0";

  tryAppendButton(contentInput, improveContentButtonClass, btn);
}

function processMailPopup(popup) {
  addGenerateTitleButton(popup.titleInput, popup.contentInput);
  addImproveEmailButton(popup.contentInput, popup.emailAccessor);
}

const observer = new MutationObserver(function (mutations, observer) {
  if (shouldRerender(mutations)) {
    const popups = getPopups();
    popups.forEach(processMailPopup);
  }
});

// define what element should be observed by the observer
// and what types of mutations trigger the callback
observer.observe(document, {
  subtree: true,
  attributes: true,
});
