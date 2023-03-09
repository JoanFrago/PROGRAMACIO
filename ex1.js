let gpuFrequency = parseInt(prompt('Freqüència del teu GPU:'));

let counter = 0;

let gameFrequency = parseInt(prompt('Freqüència del joc:'));
while (gameFrequency !== 0) {

    if (gpuFrequency >= gameFrequency) {
    
    counter++;
}

    gameFrequency = parseInt(prompt('Freqüència del joc:'));
}

console.log(`Le corre a ${counter} juegos`);
