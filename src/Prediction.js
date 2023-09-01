import React, {useState} from "react"
import axios from 'axios';

export default function Prediction() {
  const [formData, setFormData] = useState({
    Location: '',
    Soil_Type: '',
    Rainfall: '',
    Area_Cultivated: '',
    Investment: '',
  });

  const [prediction, setPrediction] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log('Sending POST request to URL:', '/api/predict');
      console.log('Sending data:', formData);

      const response = await axios.post('http://localhost:5000/api/predict', formData);

      console.log('Response from server:', response);
      
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
  };

  return (
      <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          
          <h1 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Crop Prediction and Profitability Analysis
          </h1>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" method='POST' onSubmit={handleSubmit}>
            <div>
              <label className="block text-sm font-medium leading-6 text-gray-900">
                Enter your Location
              </label>
              <div className="mt-2">
                <input
                  id="location"
                  name="Location"
                  value={formData.Location}
                  onChange={handleInputChange}
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label className="block text-sm font-medium leading-6 text-gray-900">
                  Enter Soil Type
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="soil_type"
                  name="Soil_Type"
                  value={formData.Soil_Type}
                  onChange={handleInputChange}
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label className="block text-sm font-medium leading-6 text-gray-900">
                  Average Rainfall in your Location(in mm)
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="rainfall"
                  name="Rainfall"
                  type="number"
                  value={formData.Rainfall}
                  onChange={handleInputChange}
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label className="block text-sm font-medium leading-6 text-gray-900">
                  Cultivation Land(in acres)
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="area"
                  name="Area_Cultivated"
                  type="number"
                  value={formData.Area_Cultivated}
                  onChange={handleInputChange}
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label className="block text-sm font-medium leading-6 text-gray-900">
                  Enter Investment Amount
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="investment"
                  name="Investment"
                  type="number"
                  value={formData.Investment}
                  onChange={handleInputChange}
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div className="flex items-center">
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Predict
              </button>
            </div>
          </form>

          {prediction !== null && (
            <div>
              <p>{prediction}</p>
            </div>
          )}
        </div>
      </div>
    
  )
}

  