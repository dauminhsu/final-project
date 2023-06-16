const editor = CodeMirror.fromTextArea(document.getElementById('editor'), {
    styleActiveLine: true,
    lineNumbers: true,
    lineWrapping: true,
    styleActiveSelected: true,
    mode: 'text',
    fontSize: 32
});

const defaultValue =
    'point A(-3,5)\n' +
    'point B(2,-3)\n' +
    'point C(-5,-11)\n' +
    'point D(5,7)\n' +
    'segment U(7,5) V(11,3)\n' +
    'polygon G(-5,3) H(2,8) I(8,9) J(7,-2) K(-1,-5)\n' +
    'circle O(3,3) 5';

editor.setValue(defaultValue);

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