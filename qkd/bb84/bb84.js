function randBit() {
  return Math.random() < 0.5 ? 0 : 1;
}

function basisSym(b) {
  // Return arrow icon
  return b === 0
    ? '<i data-lucide="arrow-up" class="inline-block w-5 h-5"></i>'
    : '<i data-lucide="arrow-right" class="inline-block w-5 h-5"></i>';
}

function runSimulation(eveRate = 0.0) {
  let rounds = 12;
  let aliceKey = [];
  let bobKey = [];
  let errors = 0;

  let table = `
    <div class="overflow-x-auto">
      <table class="w-full bg-zinc-800 rounded-lg overflow-hidden shadow-lg">
        <thead>
          <tr class="bg-orange-500 border-b border-zinc-700">
            <th class="px-4 py-3 text-white font-bold text-center">#</th>
            <th class="px-4 py-3 text-white font-bold text-center">Alice<br>Bit</th>
            <th class="px-4 py-3 text-white font-bold text-center">Alice<br>Base</th>
            <th class="px-4 py-3 text-white font-bold text-center">Bob<br>Base</th>
            <th class="px-4 py-3 text-white font-bold text-center">Bob<br>Bit</th>
            <th class="px-4 py-3 text-white font-bold text-center">¿Coinciden?</th>
          </tr>
        </thead>
        <tbody>`;

  for (let i = 0; i < rounds; i++) {
    let aliceBit = randBit(),
      aliceBasis = randBit(),
      bobBasis = randBit();

    // Intercepción de Eve
    let eveInter = Math.random() < eveRate;
    let photonBit, photonBasis;
    if (eveInter) {
      let eveBasis = randBit();
      let eveBit = eveBasis === aliceBasis ? aliceBit : randBit();
      photonBit = eveBit;
      photonBasis = eveBasis;
    } else {
      photonBit = aliceBit;
      photonBasis = aliceBasis;
    }

    // Medición de Bob
    let bobBit = bobBasis === photonBasis ? photonBit : randBit();
    let match = aliceBasis === bobBasis;

    table += `
      <tr class="border-b border-zinc-700 hover:bg-zinc-700 transition-colors">
        <td class="px-4 py-3 text-zinc-100 text-center border-r border-zinc-700">${
          i + 1
        }</td>
        <td class="px-4 py-3 text-zinc-100 text-center border-r border-zinc-700 font-mono">${aliceBit}</td>
        <td class="px-4 py-3 text-zinc-100 text-center border-r border-zinc-700">${basisSym(
          aliceBasis
        )}</td>
        <td class="px-4 py-3 text-zinc-100 text-center border-r border-zinc-700">${basisSym(
          bobBasis
        )}</td>
        <td class="px-4 py-3 text-zinc-100 text-center border-r border-zinc-700 font-mono">${bobBit}</td>
        <td class="px-4 py-3 text-center"> ${
          match
            ? '<i data-lucide="check" class="inline-block w-5 h-5 text-green-400"></i>'
            : '<i data-lucide="x" class="inline-block w-5 h-5 text-red-400"></i>'
        }</td>
      </tr>`;

    if (match) {
      aliceKey.push(aliceBit);
      bobKey.push(bobBit);
      if (aliceBit !== bobBit) errors++;
    }
  }
  table += `
        </tbody>
      </table>
    </div>`;

  let qber = aliceKey.length
    ? ((100 * errors) / aliceKey.length).toFixed(1)
    : 0;

  let keyInfo = `
    <div class="bg-zinc-800 rounded-xl p-6 mt-6 border border-zinc-700">
      <div class="space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center gap-2">
          <span class="text-zinc-300 font-semibold">Clave de Alice:</span>
          <span class="font-mono bg-zinc-700 text-zinc-100 px-3 py-1 rounded text-lg tracking-wider">${aliceKey.join(
            ""
          )}</span>
        </div>
        <div class="flex flex-col sm:flex-row sm:items-center gap-2">
          <span class="text-zinc-300 font-semibold">Clave de Bob:</span>
          <span class="font-mono bg-zinc-700 text-zinc-100 px-3 py-1 rounded text-lg tracking-wider">${bobKey.join(
            ""
          )}</span>
        </div>
        <div class="flex flex-col sm:flex-row sm:items-center gap-2">
          <span class="text-zinc-300 font-semibold">Longitud de la Clave:</span>
          <span class="text-zinc-100">${aliceKey.length} bits</span>
        </div>
        <div class="flex flex-col sm:flex-row sm:items-center gap-2">
          <span class="text-zinc-300 font-semibold">Tasa de Error (QBER):</span>
          <span class="${
            qber > 10 ? "text-red-400" : "text-green-400"
          } font-bold">${qber}%</span>
        </div>
        ${
          eveRate > 0
            ? `<div class="flex flex-col sm:flex-row sm:items-center gap-2">
                <span class="text-zinc-300 font-semibold">Interferencia de Eve:</span>
                <span class="text-red-400 font-bold">${(eveRate * 100).toFixed(
                  0
                )}%</span>
              </div>`
            : ""
        }
        ${
          eveRate > 0 && qber > 10
            ? `<div class="bg-red-900/20 border border-red-500/30 rounded-lg p-4 mt-4">
                <p class="text-red-400 font-bold flex items-center gap-2">
                  <i data-lucide="alert-triangle" class="w-5 h-5"></i>
                  ¡Alta tasa de error detectada! La presencia de Eve es revelada por la mecánica cuántica.
                </p>
              </div>`
            : eveRate === 0
            ? `<div class="bg-green-900/20 border border-green-500/30 rounded-lg p-4 mt-4">
                <p class="text-green-400 font-bold flex items-center gap-2">
                  <i data-lucide="check" class="w-5 h-5"></i>
                  ¡Comunicación segura establecida!
                </p>
              </div>`
            : `<div class="bg-yellow-900/20 border border-yellow-500/30 rounded-lg p-4 mt-4">
                <p class="text-yellow-400 font-bold flex items-center gap-2">
                  <i data-lucide="search" class="w-5 h-5"></i>
                  Baja tasa de error - Eve podría estar presente pero siendo cuidadosa.
                </p>
              </div>`
        }
      </div>
    </div>`;

  // Determine which output div to use
  let outputDiv = eveRate > 0 ? "simulation-output-eve" : "simulation-output";
  let targetElement = document.getElementById(outputDiv);

  if (targetElement) {
    targetElement.innerHTML = table + keyInfo;

    // Add a smooth reveal animation
    targetElement.style.opacity = "0";
    targetElement.style.transform = "translateY(20px)";

    setTimeout(() => {
      targetElement.style.transition = "all 0.6s ease";
      targetElement.style.opacity = "1";
      targetElement.style.transform = "translateY(0)";

      // Re-initialize Lucide icons for the new content
      if (typeof lucide !== "undefined") {
        lucide.createIcons();
      }
    }, 100);
  }
}
