"use client";

import React from "react";

interface CheckboxWithLabelProps {
  label: string;
  checked: boolean;
  onChange: (checked: boolean) => void;
  id?: string;
}

const CheckboxWithLabel: React.FC<CheckboxWithLabelProps> = ({ label, checked, onChange, id }) => {
  return (
    <label htmlFor={id} className="flex items-center space-x-2 cursor-pointer">
      <input
        id={id}
        type="checkbox"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        className="form-checkbox h-5 w-5 text-blue-600"
      />
      <span className="text-gray-800">{label}</span>
    </label>
  );
};

export default CheckboxWithLabel;