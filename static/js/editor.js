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
        .then(response => response.blob())
        .then(imageBlob => {
            const imageObjectURL = URL.createObjectURL(imageBlob);
            const plot = document.getElementById('plot');
            plot.src = imageObjectURL;
        });
}