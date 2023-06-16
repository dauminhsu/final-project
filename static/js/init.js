const initCheckbox = (id) => {
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.id = id;
    input.name = id;
    input.checked = (new URL(window.location.href)).searchParams.get(id) === 'true';
    input.onclick = editorSubmit;

    const div = document.createElement('div');
    div.classList.add('slider');
    div.classList.add('round');

    const checkboxContainer = document.getElementById('checkbox-container-' + id);
    checkboxContainer.appendChild(input);
    checkboxContainer.appendChild(div);
}

window.onload = () => {
    initCheckbox('show-line');
    initCheckbox('show-label');
}