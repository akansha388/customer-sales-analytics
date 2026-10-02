import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LayoutDashboard, BarChart3, Users, PieChart, ShoppingBag, MapPin, FileSpreadsheet } from 'lucide-react';

interface Metrics {
  total_revenue: number;
  total_orders: number;
  total_customers: number;
  average_order_value: number;
}

export default function App() {
  const [metrics, setMetrics] = useState<Metrics | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/dashboard/summary')
      .then((res) => {
        setMetrics(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("API error:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="flex h-screen bg-ivory font-serif text-charcoal">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-beige p-6 flex flex-col justify-between">
        <div>
          <h1 className="text-xl font-bold tracking-tight mb-8 text-charcoal border-b border-beige pb-4">
            Analytics Platform
          </h1>
          <nav className="space-y-2">
            <a href="#" className="flex items-center gap-3 px-3 py-2 rounded bg-beige text-forest font-semibold">
              <LayoutDashboard size={18} /> Overview
            </a>
            <a href="#" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-beige text-charcoal">
              <BarChart3 size={18} /> Sales Analytics
            </a>
            <a href="#" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-beige text-charcoal">
              <Users size={18} /> Customers
            </a>
            <a href="#" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-beige text-charcoal">
              <PieChart size={18} /> RFM Segmentation
            </a>
            <a href="#" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-beige text-charcoal">
              <ShoppingBag size={18} /> Products
            </a>
            <a href="#" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-beige text-charcoal">
              <MapPin size={18} /> Regional
            </a>
            <a href="#" className="flex items-center gap-3 px-3 py-2 rounded hover:bg-beige text-charcoal">
              <FileSpreadsheet size={18} /> Transactions
            </a>
          </nav>
        </div>
        <div className="text-xs text-slate border-t border-beige pt-4">
          Enterprise Business Intelligence v1.0
        </div>
      </aside>

      {/* Main View */}
      <main className="flex-1 overflow-y-auto p-8">
        <header className="mb-8 flex justify-between items-center border-b border-beige pb-4">
          <div>
            <h2 className="text-2xl font-bold">Executive Overview</h2>
            <p className="text-sm text-slate">Live business metrics powered by PostgreSQL & FastAPI.</p>
          </div>
          <button className="px-4 py-2 bg-forest text-white rounded shadow-sm hover:opacity-90">
            Export Report
          </button>
        </header>

        {/* KPI Grid */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <div className="bg-white p-5 border border-beige rounded shadow-sm">
            <div className="text-sm text-slate">Total Revenue</div>
            <div className="text-2xl font-bold text-charcoal mt-1">
              {loading ? "..." : `$${metrics?.total_revenue.toLocaleString()}`}
            </div>
          </div>
          <div className="bg-white p-5 border border-beige rounded shadow-sm">
            <div className="text-sm text-slate">Total Orders</div>
            <div className="text-2xl font-bold text-charcoal mt-1">
              {loading ? "..." : metrics?.total_orders.toLocaleString()}
            </div>
          </div>
          <div className="bg-white p-5 border border-beige rounded shadow-sm">
            <div className="text-sm text-slate">Total Customers</div>
            <div className="text-2xl font-bold text-charcoal mt-1">
              {loading ? "..." : metrics?.total_customers.toLocaleString()}
            </div>
          </div>
          <div className="bg-white p-5 border border-beige rounded shadow-sm">
            <div className="text-sm text-slate">Average Order Value</div>
            <div className="text-2xl font-bold text-charcoal mt-1">
              {loading ? "..." : `$${metrics?.average_order_value}`}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}