class CreateReads < ActiveRecord::Migration[6.1]
  def change
    create_table :reads do |t|
      t.decimal :temperature, precision: 12, scale: 2

      t.timestamps
    end
  end
end
