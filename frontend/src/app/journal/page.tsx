import { Clock } from 'lucide-react';

export default function Journal () {
  return (
    <div className="flex flex-col items-center  h-screen mt-5">
      <h1 className="text-2xl font-bold mb-4">Journal</h1>
      <div className="">
        <div className="bg-gray-300 px-8 py-16 rounded-lg shadow-md">
          <p><span className="text-lg">+</span> New Journal</p>
        </div>
      </div>
      <div className="mx-8 my-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div className="rounded-lg shadow-md py-3">
          <div className="flex flex-row gap-2 items-center bg-blue-400 px-2 py-1">
            <Clock color="white" size={18}/>
            <p className="text-white text-sm">2023-10-01</p>
          </div>
          <p className="font-bold py-3">Title</p>
          <p className="text-sm text-gray-700">This is a journal entry. It can be a long text, but for now, it is just a demo text.</p>
        </div>
        <div className="rounded-lg shadow-md py-3">
          <div className="flex flex-row gap-2 items-center bg-blue-400 px-2 py-1">
            <Clock color="white" size={18}/>
            <p className="text-white text-sm">2023-10-01</p>
          </div>
          <p className="font-bold py-3">Title</p>
          <p className="text-sm text-gray-700">This is a journal entry. It can be a long text, but for now, it is just a demo text.</p>
        </div>
        <div className="rounded-lg shadow-md py-3">
          <div className="flex flex-row gap-2 items-center bg-blue-400 px-2 py-1">
            <Clock color="white" size={18}/>
            <p className="text-white text-sm">2023-10-01</p>
          </div>
          <p className="font-bold py-3">Title</p>
          <p className="text-sm text-gray-700">This is a journal entry. It can be a long text, but for now, it is just a demo text.</p>
        </div>
      </div>
    </div>
  );
}