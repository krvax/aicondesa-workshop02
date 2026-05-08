/* ===================================================
   POMODORO TIMER — script.js
   =================================================== */

const MODES = {
  focus: { label: 'Time to focus 🌿', minutes: 25, bodyClass: '' },
  short: { label: 'Short break ☕',   minutes: 5,  bodyClass: 'mode-short' },
  long:  { label: 'Long break 🌙',    minutes: 15, bodyClass: 'mode-long' },
};

const QUOTES = [
  '"The secret of getting ahead is getting started." — Mark Twain',
  '"Focus on being productive instead of busy." — Tim Ferriss',
  '"Small steps every day lead to big changes." — Unknown',
  '"You don\'t have to be great to start, but you have to start to be great." — Zig Ziglar',
  '"Almost everything will work if you unplug it for a few minutes." — Anne Lamott',
  '"Rest is not idleness." — John Lubbock',
  '"The key is not to prioritize your schedule but to schedule your priorities." — S. Covey',
];

// State
let currentMode = 'focus';
let totalSeconds = MODES.focus.minutes * 60;
let secondsLeft  = totalSeconds;
let isRunning    = false;
let interval     = null;
let sessionIndex = 0; // 0-3
let completedSessions = 0;

// DOM refs
const timeDisplay  = document.getElementById('timeDisplay');
const modeLabel    = document.getElementById('modeLabel');
const btnLabel     = document.getElementById('btnLabel');
const ringProgress = document.getElementById('ringProgress');
const sessionCount = document.getElementById('sessionCount');
const quoteText    = document.getElementById('quoteText');

const CIRCUMFERENCE = 2 * Math.PI * 96; // r=96 → ≈ 603.19

// ===================================================
// INIT
// ===================================================
function init() {
  updateRing(1);
  renderDots();
  rotateQuote();
}

// ===================================================
// MODE SWITCHING
// ===================================================
function switchMode(mode) {
  clearInterval(interval);
  isRunning = false;
  currentMode = mode;

  const config = MODES[mode];
  totalSeconds = config.minutes * 60;
  secondsLeft  = totalSeconds;

  updateDisplay();
  updateRing(1);
  modeLabel.textContent = config.label;
  btnLabel.textContent = 'Start';

  // Update body class for color theme
  document.body.classList.remove('mode-short', 'mode-long');
  if (config.bodyClass) document.body.classList.add(config.bodyClass);

  // Update active tab
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById(`tab-${mode}`).classList.add('active');
}

// ===================================================
// TIMER CONTROL
// ===================================================
function toggleTimer() {
  if (isRunning) {
    pauseTimer();
  } else {
    startTimer();
  }
}

function startTimer() {
  isRunning = true;
  btnLabel.textContent = 'Pause';
  rotateQuote();

  interval = setInterval(() => {
    if (secondsLeft <= 0) {
      completeSession();
      return;
    }
    secondsLeft--;
    updateDisplay();
    updateRing(secondsLeft / totalSeconds);
  }, 1000);
}

function pauseTimer() {
  isRunning = false;
  clearInterval(interval);
  btnLabel.textContent = 'Resume';
}

function resetTimer() {
  clearInterval(interval);
  isRunning = false;
  secondsLeft = totalSeconds;
  updateDisplay();
  updateRing(1);
  btnLabel.textContent = 'Start';
}

function skipSession() {
  clearInterval(interval);
  secondsLeft = 0;
  completeSession();
}

// ===================================================
// COMPLETE A SESSION
// ===================================================
function completeSession() {
  clearInterval(interval);
  isRunning = false;
  playDing();

  if (currentMode === 'focus') {
    completedSessions++;
    sessionIndex = (sessionIndex + 1) % 4;
    sessionCount.textContent = completedSessions + 1;
    renderDots();

    // After 4 focus sessions → suggest long break
    if (completedSessions % 4 === 0) {
      switchMode('long');
    } else {
      switchMode('short');
    }
  } else {
    switchMode('focus');
  }

  rotateQuote();
}

// ===================================================
// UI UPDATES
// ===================================================
function updateDisplay() {
  const m = Math.floor(secondsLeft / 60).toString().padStart(2, '0');
  const s = (secondsLeft % 60).toString().padStart(2, '0');
  timeDisplay.textContent = `${m}:${s}`;
  document.title = `${m}:${s} — Pomodoro`;
}

function updateRing(fraction) {
  const offset = CIRCUMFERENCE * (1 - fraction);
  ringProgress.style.strokeDasharray  = CIRCUMFERENCE;
  ringProgress.style.strokeDashoffset = offset;
}

function renderDots() {
  for (let i = 0; i < 4; i++) {
    const dot = document.getElementById(`dot-${i}`);
    dot.classList.remove('active', 'done');
    if (i < sessionIndex) dot.classList.add('done');
    if (i === sessionIndex) dot.classList.add('active');
  }
}

function rotateQuote() {
  const q = QUOTES[Math.floor(Math.random() * QUOTES.length)];
  quoteText.style.opacity = '0';
  setTimeout(() => {
    quoteText.textContent = `"${q}"`;
    quoteText.style.opacity = '0.85';
    quoteText.style.transition = 'opacity 0.6s ease';
  }, 300);
}

// ===================================================
// SOUND — gentle ding using Web Audio API
// ===================================================
function playDing() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    // First tone
    const osc1 = ctx.createOscillator();
    const gain1 = ctx.createGain();
    osc1.connect(gain1); gain1.connect(ctx.destination);
    osc1.frequency.value = 830;
    osc1.type = 'sine';
    gain1.gain.setValueAtTime(0.3, ctx.currentTime);
    gain1.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);
    osc1.start(ctx.currentTime);
    osc1.stop(ctx.currentTime + 1.2);

    // Harmony
    const osc2 = ctx.createOscillator();
    const gain2 = ctx.createGain();
    osc2.connect(gain2); gain2.connect(ctx.destination);
    osc2.frequency.value = 1046;
    osc2.type = 'sine';
    gain2.gain.setValueAtTime(0.15, ctx.currentTime + 0.15);
    gain2.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.5);
    osc2.start(ctx.currentTime + 0.15);
    osc2.stop(ctx.currentTime + 1.5);
  } catch(e) {
    // Audio not available — fail silently
  }
}

// ===================================================
// KEYBOARD SHORTCUTS
// ===================================================
document.addEventListener('keydown', (e) => {
  if (e.code === 'Space' && e.target === document.body) {
    e.preventDefault();
    toggleTimer();
  }
  if (e.code === 'KeyR') resetTimer();
  if (e.code === 'Digit1') switchMode('focus');
  if (e.code === 'Digit2') switchMode('short');
  if (e.code === 'Digit3') switchMode('long');
});

// ===================================================
// START
// ===================================================
init();
