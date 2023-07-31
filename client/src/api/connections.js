let socket;

if (typeof window !== 'undefined') {
  socket = new WebSocket('ws://localhost:8000/ws');
}

export { socket };