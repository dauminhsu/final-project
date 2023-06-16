const download = () => {
    const link = document.createElement('a');
    link.href = document.getElementById('plot').src;
    link.download = 'plot.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
