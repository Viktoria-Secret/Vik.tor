'use client'
import React from "react";

interface RankCardProps {
  label: string;
  colorClass: string; // Tailwind background color class for the indicator
  onClick?: () => void;
}

export default function RankCard({ label, colorClass, onClick }: RankCardProps) {
  return (
    <button
      onClick={onClick}
      className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow flex items-center p-4 w-full text-left"
    >
      {/* Color indicator */}
      <span
        className={`inline-block w-3 h-3 rounded-full mr-3 ${colorClass}`}
      />
      {/* Rank label */}
      <span className="font-medium text-gray-800">{label}</span>
    </button>
  );
} 