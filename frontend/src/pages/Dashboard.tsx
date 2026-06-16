import { Sidebar } from "../components/Sidebar";

export default function Dashboard() {
  return (
    <main className="app-shell">
      <Sidebar />
      <section className="content">
        <header className="page-header">
          <h1>Dashboard</h1>
          <button>Create Invoice</button>
        </header>
        <section className="kpi-grid">
          <article>Revenue<br /><strong>₱185,000</strong></article>
          <article>Expenses<br /><strong>₱62,400</strong></article>
          <article>Profit<br /><strong>₱122,600</strong></article>
          <article>Cash Balance<br /><strong>₱410,300</strong></article>
        </section>
      </section>
    </main>
  );
}
