import express from "express";
import path from "path";
import { createServer as createViteServer } from "vite";
import fs from "fs";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PORT = parseInt(process.env.PORT || "3000", 10);
const HOST = process.env.HOST || "0.0.0.0";
const isProd = process.env.NODE_ENV === "production" || !fs.existsSync(path.join(__dirname, "src"));

async function startServer() {
  const app = express();
  app.use(express.json());

  // Health check
  app.get("/api/health", (_req, res) => res.json({ ok: true, ts: Date.now() }));

  if (!isProd) {
    // Dev: use Vite middleware. HMR fully disabled to prevent WebSocket errors.
    const vite = await createViteServer({
      server: { middlewareMode: true, hmr: false, watch: null },
      appType: "spa",
      logLevel: "info",
    });
    app.use(vite.middlewares);
  } else {
    // Prod: serve built static files from dist/
    const distPath = path.join(__dirname, "dist");
    app.use(express.static(distPath, { maxAge: "1y", index: false }));
    app.get("*", (_req, res) => res.sendFile(path.join(distPath, "index.html")));
  }

  app.listen(PORT, HOST, () => {
    console.log(`PRF Dota 2 server running on http://${HOST}:${PORT} (${isProd ? "production" : "dev"})`);
  });
}

startServer().catch((err) => {
  console.error("Failed to start server:", err);
  process.exit(1);
});
