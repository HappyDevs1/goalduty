export default function Journaling () {
  return (
    <div className="flex flex-col items-center justify-center">
      <h1 className="text-2xl font-bold mt-5">Journal</h1>
      <p className="text-sm text-gray-700 max-w-95">
        This is the journaling page.</p>
        <div className="my-15 bg-gray-200 px-8 py-16 rounded-lg shadow-md">
          <p>Type or record to start journaling.</p>
        </div>
    </div>
  )
}