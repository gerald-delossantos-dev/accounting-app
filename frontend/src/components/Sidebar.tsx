export const navItems = [
  "Dashboard", "Invoices", "Customers", "Expenses", "Vendors", "Banking", "Accounting", "Reports", "Settings"
];

export function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="brand">LedgerPro</div>
      <nav>{navItems.map(item => <a key={item}>{item}</a>)}</nav>
    </aside>
  );
}
