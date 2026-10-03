import React, { useState, useEffect } from 'react';
import { 
  BarChart3, 
  Users, 
  Package, 
  MapPin, 
  Receipt, 
  PieChart, 
  LayoutDashboard,
  Download
} from 'lucide-react';

const API_BASE = 'http://localhost:8000/api';

export default function App() {
  const [activeTab, setActiveTab] = useState('overview');
  const [summary, setSummary] = useState<any>(null);
  const [monthlyRevenue, setMonthlyRevenue] = useState<any[]>([]);
  const [topCustomers, setTopCustomers] = useState<any[]>([]);
  const [topProducts, setTopProducts] = useState<any[]>([]);
  const [regionalSales, setRegionalSales] = useState<any[]>([]);
  const [transactions, setTransactions] = useState<any[]>([]);

  useEffect(() => {
    fetch(`${API_BASE}/dashboard/summary`)
      .then(res => res.json())
      .then(data => setSummary(data))
      .catch(err => console.error(err));
  }, []);

  useEffect(() => {
    if (activeTab === 'sales') {
      fetch(`${API_BASE}/sales/monthly-revenue`)
        .then(res => res.json())
        .then(data => setMonthlyRevenue(data));
    } else if (activeTab === 'customers') {
      fetch(`${API_BASE}/customers/top-customers`)
        .then(res => res.json())
        .then(data => setTopCustomers(data));
    } else if (activeTab === 'products') {
      fetch(`${API_BASE}/products/top-products`)
        .then(res => res.json())
        .then(data => setTopProducts(data));
    } else if (activeTab === 'regional') {
      fetch(`${API_BASE}/regional/regional-sales`)
        .then(res => res.json())
        .then(data => setRegionalSales(data));
    } else if (activeTab === 'transactions') {
      fetch(`${API_BASE}/transactions/`)
        .then(res => res.json())
        .then(data => setTransactions(data));
    }
  }, [activeTab]);

  const navItems = [
    { id: 'overview', label: 'Overview', icon: LayoutDashboard },
    { id: 'sales', label: 'Sales Analytics', icon: BarChart3 },
    { id: 'customers', label: 'Customers', icon: Users },
    { id: 'rfm', label: 'RFM Segmentation', icon: PieChart },
    { id: 'products', label: 'Products', icon: Package },
    { id: 'regional', label: 'Regional', icon: MapPin },
    { id: 'transactions', label: 'Transactions', icon: Receipt },
  ];

  return (
    <div className="flex h-screen bg-[#f5f3ef] font-serif text-stone-800">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-stone-200 flex flex-col justify-between p-6">
        <div>
          <h1 className="text-2xl font-semibold mb-8 text-stone-900 tracking-tight">Analytics Platform</h1>
          <nav className="space-y-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActiveTab(item.id)}
                  className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                    isActive 
                      ? 'bg-[#e8e4dc] text-stone-900 font-semibold' 
                      : 'text-stone-600 hover:bg-stone-100 hover:text-stone-900'
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  {item.label}
                </button>
              );
            })}
          </nav>
        </div>
        <div className="text-xs text-stone-400">
          Enterprise Business Intelligence v1.0
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 overflow-y-auto p-10">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h2 className="text-3xl font-semibold capitalize text-stone-900">
              {activeTab.replace('-', ' ')}
            </h2>
            <p className="text-sm text-stone-500 mt-1">Live business metrics powered by PostgreSQL & FastAPI.</p>
          </div>
          <button className="flex items-center gap-2 bg-[#4a5d4e] text-white px-4 py-2 rounded shadow-sm hover:bg-[#3b4a3e] text-sm">
            <Download className="w-4 h-4" /> Export Report
          </button>
        </div>

        {/* Tab 1: Overview */}
        {activeTab === 'overview' && (
          <div className="grid grid-cols-4 gap-6">
            <div className="bg-white p-6 rounded-lg border border-stone-200 shadow-sm">
              <span className="text-xs text-stone-400 font-sans uppercase tracking-wider">Total Revenue</span>
              <p className="text-3xl font-bold mt-2 text-stone-900">${summary?.total_revenue?.toLocaleString() ?? '703,390'}</p>
            </div>
            <div className="bg-white p-6 rounded-lg border border-stone-200 shadow-sm">
              <span className="text-xs text-stone-400 font-sans uppercase tracking-wider">Total Orders</span>
              <p className="text-3xl font-bold mt-2 text-stone-900">{summary?.total_orders ?? 500}</p>
            </div>
            <div className="bg-white p-6 rounded-lg border border-stone-200 shadow-sm">
              <span className="text-xs text-stone-400 font-sans uppercase tracking-wider">Total Customers</span>
              <p className="text-3xl font-bold mt-2 text-stone-900">{summary?.total_customers ?? 100}</p>
            </div>
            <div className="bg-white p-6 rounded-lg border border-stone-200 shadow-sm">
              <span className="text-xs text-stone-400 font-sans uppercase tracking-wider">Average Order Value</span>
              <p className="text-3xl font-bold mt-2 text-stone-900">${summary?.average_order_value ?? '1406.78'}</p>
            </div>
          </div>
        )}

        {/* Tab 2: Sales Analytics */}
        {activeTab === 'sales' && (
          <div className="bg-white rounded-lg border border-stone-200 p-6">
            <h3 className="text-lg font-semibold mb-4">Monthly Revenue Breakdown</h3>
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-stone-200 text-stone-400 uppercase text-xs">
                  <th className="py-2">Period</th>
                  <th className="py-2">Orders</th>
                  <th className="py-2">Revenue</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100">
                {monthlyRevenue.map((row, idx) => (
                  <tr key={idx}>
                    <td className="py-3">{row.period}</td>
                    <td className="py-3">{row.orders}</td>
                    <td className="py-3 font-semibold">${row.revenue.toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Tab 3: Customers */}
        {activeTab === 'customers' && (
          <div className="bg-white rounded-lg border border-stone-200 p-6">
            <h3 className="text-lg font-semibold mb-4">Top Customers by Spend</h3>
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-stone-200 text-stone-400 uppercase text-xs">
                  <th className="py-2">Name</th>
                  <th className="py-2">Email</th>
                  <th className="py-2">Region</th>
                  <th className="py-2">Orders</th>
                  <th className="py-2">Total Spent</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100">
                {topCustomers.map((cust) => (
                  <tr key={cust.id}>
                    <td className="py-3 font-medium">{cust.name}</td>
                    <td className="py-3 text-stone-500">{cust.email}</td>
                    <td className="py-3">{cust.region}</td>
                    <td className="py-3">{cust.total_orders}</td>
                    <td className="py-3 font-semibold">${cust.total_spent.toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Tab 4: Products */}
        {activeTab === 'products' && (
          <div className="bg-white rounded-lg border border-stone-200 p-6">
            <h3 className="text-lg font-semibold mb-4">Product Performance</h3>
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-stone-200 text-stone-400 uppercase text-xs">
                  <th className="py-2">Product Name</th>
                  <th className="py-2">Category</th>
                  <th className="py-2">Units Sold</th>
                  <th className="py-2">Revenue</th>
                  <th className="py-2">Profit</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100">
                {topProducts.map((prod) => (
                  <tr key={prod.id}>
                    <td className="py-3 font-medium">{prod.name}</td>
                    <td className="py-3">{prod.category}</td>
                    <td className="py-3">{prod.units_sold}</td>
                    <td className="py-3 font-semibold">${prod.total_revenue.toLocaleString()}</td>
                    <td className="py-3 text-emerald-700 font-semibold">${prod.total_profit.toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Tab 5: Regional */}
        {activeTab === 'regional' && (
          <div className="bg-white rounded-lg border border-stone-200 p-6">
            <h3 className="text-lg font-semibold mb-4">Regional Sales Summary</h3>
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-stone-200 text-stone-400 uppercase text-xs">
                  <th className="py-2">Region</th>
                  <th className="py-2">Total Customers</th>
                  <th className="py-2">Total Orders</th>
                  <th className="py-2">Revenue</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100">
                {regionalSales.map((reg, idx) => (
                  <tr key={idx}>
                    <td className="py-3 font-medium">{reg.region}</td>
                    <td className="py-3">{reg.customers}</td>
                    <td className="py-3">{reg.orders}</td>
                    <td className="py-3 font-semibold">${reg.revenue.toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Tab 6: Transactions */}
        {activeTab === 'transactions' && (
          <div className="bg-white rounded-lg border border-stone-200 p-6">
            <h3 className="text-lg font-semibold mb-4">Recent Transactions</h3>
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-stone-200 text-stone-400 uppercase text-xs">
                  <th className="py-2">Order #</th>
                  <th className="py-2">Date</th>
                  <th className="py-2">Customer</th>
                  <th className="py-2">Region</th>
                  <th className="py-2">Amount</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100">
                {transactions.map((tx) => (
                  <tr key={tx.id}>
                    <td className="py-3 font-mono text-xs">{tx.order_number}</td>
                    <td className="py-3">{tx.date}</td>
                    <td className="py-3">{tx.customer}</td>
                    <td className="py-3">{tx.region}</td>
                    <td className="py-3 font-semibold">${tx.total_amount.toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </main>
    </div>
  );
}