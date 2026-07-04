interface Props {

    title: string;

    value: string | number;

}

export default function DashboardCard({

    title,

    value,

}: Props) {

    return (

        <div className="bg-white rounded-xl shadow p-5">

            <h2 className="text-gray-500">

                {title}

            </h2>

            <h1 className="text-3xl font-bold">

                {value}

            </h1>

        </div>

    );

}