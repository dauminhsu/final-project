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

const editorUndo = () => {
    editor.undo();
}

const editorRedo = () => {
    editor.redo();
}

const editorReset = () => {
    editor.setValue(defaultValue);
}

const editorClear = () => {
    editor.setValue('');
}

const editorSubmit = () => {
    const url = new URL(window.location.href);
    url.searchParams.set('show-line', document.getElementById('show-line').checked);
    url.searchParams.set('show-label', document.getElementById('show-label').checked);
    fetch(url.href, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: editor.getValue()})
    })
        .then(response => response.text())
        .then(imageName => {
            const plot = document.getElementById('plot');
            plot.src = imageName;
        });
}
